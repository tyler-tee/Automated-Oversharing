import json
import re
import requests
import os
from flask import (Blueprint, current_app, redirect, render_template,
                   request, session)
import markdown
from sqlmodel import Session
from ..models import Entry

blog_pages = Blueprint("blog", __name__)

def notify_tines_of_post(title, content, slug, tags_str):
    """Load the Tines config and notify Tines of a new post."""
    config_path = os.path.join(os.path.dirname(__file__), "config/config.json")
    try:
        with open(config_path, 'r') as f:
            tines_config = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return  # Stop if config can't be loaded

    try:
        requests.post(
            tines_config['TINES_WEBHOOK'],
            headers={"Authorization": f"Bearer {tines_config['TINES_SECRET']}"},
            json={"title": title, "content": content, "slug": slug, "tags": tags_str},
            timeout=10
        )
    except requests.exceptions.RequestException:
        return  # Fail silently if request fails

@blog_pages.route('/blog/create/', methods=["GET", "POST"])
def create_page():
    if request.method == "POST":
        title = request.form.get("inputTitle")
        content = request.form.get("post")
        slug = re.sub(r'[^\w]+', '-', title.lower())
        tags_list = request.form.getlist("tags")
        tags_str = ",".join(tags_list)
        published = 'publish' in request.form

        post = Entry(title=title, content=content, slug=slug, tags=tags_str, published=published)
        with Session(current_app.engine) as db_session:
            db_session.add(post)
            db_session.commit()

        if published:
            notify_tines_of_post(title, content, slug, tags_str)

        return redirect(f'/blog/{slug}' if published else '/blog/drafts')

    return redirect('/blog')

@blog_pages.route('/blog')
def blog():
    with Session(current_app.engine) as db_session:
        articles = db_session.query(Entry).filter(Entry.published == True).all()

    articles = [dict(article) for article in articles]
    for article in articles:
        article['content_html'] = markdown.markdown(article['content'][:500])

    return render_template('blog.html', articles=articles)
