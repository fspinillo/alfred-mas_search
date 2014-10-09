import sys
from workflow import Workflow, ICON_WEB, web

log = None

def main(wf):

    if len(wf.args):
        query = wf.args[0]

        appStore = web.get('https://itunes.apple.com/search?term=' + query + '&entity=macSoftware&limit=10').json()

        for storeResults in appStore['results']:
            masURL = storeResults['trackViewUrl'].replace('https://', 'macappstore://')
            wf.add_item(title = 'Name: %s' % (storeResults['trackCensoredName']),
                subtitle = storeResults['description'],
                arg = masURL,
                valid = True
                )

        wf.send_feedback()

if __name__ == '__main__':
    wf = Workflow()
    sys.exit(wf.run(main))