from crypt import methods
from flask import render_template,request,redirect,url_for
from . import main
from app import db
from ..models import Tracker,Logs
from ..forms import tracker_form,logForm

# Views
@main.route('/',methods=['GET', 'POST'])
def index():

    '''
    View root page function that returns the index page and its data
    '''
    form=tracker_form()
    trackers=Tracker.query.all() 
    if form.validate_on_submit():
        tracker_name=form.tracker_name.data
        comment=form.comment.data
        rate=form.rate.data

        #update tracker instancs
        tracker = Tracker(tracker_name=tracker_name,comment=comment,rate=rate)

        tracker.save_tracker()
        return redirect(url_for('main.index'))
    return render_template('index.html',form=form,trackers=trackers)

@main.route('/logs/<int:id>',methods=['GET','POST'])
def log(id):
    '''
    View movie page function that returns the movie details page and its data
    '''
    form=logForm()
    logs = Logs.query.get(id)
    if form.validate_on_submit():
        name=form.name.data
        comment=form.comment.data
        rate=form.rate.data

        logs = Logs(id=logs.id,name=name,comment=comment,rate=rate)

        logs.save_log()
        return redirect(url_for('main.log',id=logs.id))
    return render_template('logs.html', logs=logs, form=form)