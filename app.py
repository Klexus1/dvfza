import logging
import os
import subprocess
import sys
import uuid

from flask import Flask, request, flash, redirect, render_template, send_file

from config import Config

app = Flask(__name__)

# logging
app.logger.setLevel(logging.DEBUG)
stream_handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(formatter)
app.logger.addHandler(stream_handler)


app.config.from_object(Config)


@app.route('/', methods=["GET", "POST"])
def upload_file():  # put application's code here
    app.logger.debug(f"received request")
    archive_uuid = ""
    if request.method == 'POST':
        if 'files' not in request.files:
            app.logger.debug('No file part')
            return redirect(request.url)
        file = request.files['files']
        if file:
            app.logger.debug('We have a file(s).')
            uploaded_files = request.files.getlist('files')
            for uploaded_file in uploaded_files:
                app.logger.debug(f"{uploaded_file.filename}")
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename))
            archive_uuid = uuid.uuid4()

            # safe version
            # app.logger.debug(f'Executed command: {["zip", f"archives/{archive_uuid}.zip"] + ["uploads/" + f.filename for f in uploaded_files]}')
            # subprocess.run(["zip", f"archives/{archive_uuid}.zip"] + ["uploads/" + f.filename for f in uploaded_files])

            # vulnerable version
            # for f in uploaded_files:
            app.logger.debug(f'/bin/sh -c pwd && ls -la && cd {app.config["UPLOAD_FOLDER"]} && zip ../archives/{archive_uuid}.zip {" ".join([f.filename for f in uploaded_files])}')
            zipper = [f"/bin/sh -c pwd && ls -la && cd {app.config['UPLOAD_FOLDER']} && zip ../archives/{archive_uuid}.zip {' '.join([f.filename for f in uploaded_files])}"]
            subprocess.run(zipper, shell=True)

    files = os.listdir("uploads")
    return render_template('index.html', files=files, zip_file_path=f"{archive_uuid}.zip")


@app.route('/download/<filename>')
def download(filename):
    print(f"about to download file {filename}")
    return send_file("archives/" + filename.lstrip("/download/"), as_attachment=True)


if __name__ == '__main__':
    app.run()
