from crypt import methods
from flask import render_template,request,redirect,url_for
from . import main
from app import db
from ..models import Tracker,Logs
from ..forms import tracker_form,logForm

# Views
@main.route('/',methods=['GET', 'POST'])
def index():
    form=tracker_form()
    trackers=Tracker.query.all() 
    if form.validate_on_submit():
        tracker_name=form.tracker_name.data
        comment=form.comment.data

        #update tracker instancs
        tracker = Tracker(tracker_name=tracker_name,comment=comment)

        tracker.save_tracker()
        return redirect(url_for('main.index'))
    return render_template('index.html',form=form,trackers=trackers)

@main.route('/logs/<int:id>',methods=['GET','POST'])
def logs(id):
    form=logForm()
    logs = Logs.query.filter_by(tracker_id=id)
    if form.validate_on_submit():
        name=form.name.data
        comment=form.comment.data
        rate=form.rate.data
        tracker_id=id
        logs = Logs(name=name,comment=comment,rate=rate,tracker_id=tracker_id)
        logs.save_log()
        return redirect(url_for('.logs',id=id))
    return render_template('logs.html', logs=logs, form=form)