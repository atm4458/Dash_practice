from flask import Blueprint, flash, render_template, redirect, url_for, session
from custom_form import InitForm
import os
import db_process

base_app = Blueprint("base_app", __name__, template_folder="template")

@base_app.route('/', methods=["GET", "POST"])
def main():
    form = InitForm()
    if form.validate_on_submit():
        user_folder = os.path.join(os.getcwd(), form.user.data)
        if not os.path.exists(user_folder):
            os.mkdir(user_folder)
        project_folder = os.path.join(os.getcwd(), form.user.data, form.project.data)
        folder = db_process.create_folder(project_folder)
        is_folder_valid = not (folder is None)
        is_file_upload = not (form.files.data[0].filename == "")
        
        if is_folder_valid and is_file_upload:
            db_process.save_files(form.files.data, project_folder)
            pickle_files = db_process.read_files(folder)
            db_process.combine_pickle(pickle_files)
            session["user_name"] = form.user.data
            session["project_name"] = form.project.data
            return redirect(url_for("/dashboard/"))
        else:
            if not is_folder_valid:
                flash("Project name已經存在, 請換一個名稱")
            if not is_file_upload:
                flash("沒有上傳Pickle files")
    return render_template("index.html", form = form)