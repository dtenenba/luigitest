import sciluigi
import slbatchwrapper
arn = "arn:aws:batch:us-west-2:064561331775:job-definition/dtenenba-scratchy:1"
task = slbatchwrapper.BatchTask(arn)
import batchwrapper
oldtask = batchwrapper.BatchTask(arn)
import sciluigi
st = sciluigi.Task()
task = sciluigi.new_task('botch', sciluigi.BatchTask)
task = sciluigi.new_task('botch', slbatchwrapper.BatchTask)
task = sciluigi.new_task('botch', slbatchwrapper.BatchTask, 'foo')
task = sciluigi.new_task('botch', slbatchwrapper.BatchTask, 'foo', job_definition=arn)
task
#%hist
