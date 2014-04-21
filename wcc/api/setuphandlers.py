from collective.grok import gs
from wcc.api import MessageFactory as _

@gs.importstep(
    name=u'wcc.api', 
    title=_('wcc.api import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('wcc.api.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
