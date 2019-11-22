from flask import Flask, request, send_file
from redis import Redis
from rq import Queue
from rq.job import Job
from rq.exceptions import NoSuchJobError
from shutil import make_archive
from waitress import serve

from tasks import scrap_text, download_images


app = Flask(__name__)
redis = Redis(host = 'redis')
queue = Queue(connection = redis)


@app.route("/add_task/<type>", methods = ['POST'])
def add_task(type):
    if not request.args.get("url"):
        return "Url not specified"
    if type == "text":
        job = queue.enqueue(scrap_text, request.args.get("url"))
        return f"Task {job.id} of type {type} added to queue at \
            {job.enqueued_at}. {len(queue)} tasks in the queue"
    elif type == "images":
        job = queue.enqueue(download_images, request.args.get("url"))
        return f"Task {job.id} of type {type} added to queue at \
            {job.enqueued_at}. {len(queue)} tasks in the queue"


@app.route("/check_status/<id>", methods = ['GET'])
def check_status(id):
    try:
        job = Job.fetch(id, connection = redis)
        return job.get_status()
    except NoSuchJobError:
        return 'There was no such job'



@app.route("/get_page/<path:url>", methods = ['GET'])
def get_page(url):
    zip_file = make_archive(url, 'zip', f"data/{url}")
    return send_file(zip_file,
        mimetype = 'application/zip',
        as_attachment = True,
        attachment_filename = f"{url}.zip"
    )


if __name__ == "__main__":
    serve(app, port = 5000)
