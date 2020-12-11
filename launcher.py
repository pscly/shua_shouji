from airtest.cli.runner import run_script
from airtest.cli.parser import runner_parser
from airtest.core.settings import Settings as ST
# 假如脚本在IDE中运行，IDE会自动帮忙加载AirtestCase。假如要用命令行独立运行脚本，则需要手工import AirtestCase
if not global().get("AirtestCase"):
    from airtest.cli.runner import AirtestCase

class CustomAirtestCase(AirtestCase):
    def __init__(self):
        super(CustomAirtestCase, self).__init__()

    def setUp(self):
        print("custom setup")
        super(CustomAirtestCase, self).setUp()

    def tearDown(self):
        print("custom tearDown")
        super(CustomAirtestCase, self).tearDown()

if __name__ == '__main__':
    ap = runner_parser()
    args = ap.parse_args()
    run_script(args, CustomAirtestCase)