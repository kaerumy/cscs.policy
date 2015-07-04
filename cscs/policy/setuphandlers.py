from collective.grok import gs
from cscs.policy import MessageFactory as _

@gs.importstep(
    name=u'cscs.policy', 
    title=_('cscs.policy import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('cscs.policy.marker.txt') is None:
        return
    portal = context.getSite()
    # do anything here
