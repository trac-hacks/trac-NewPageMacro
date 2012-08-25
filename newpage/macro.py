# vim: expandtab
import re, time
from StringIO import StringIO

from genshi.builder import tag

from trac.core import *
from trac.wiki.formatter import format_to_html, format_to_oneliner
from trac.util import TracError
from trac.util.text import to_unicode
from trac.web.chrome import Chrome, add_stylesheet, ITemplateProvider
from trac.wiki.api import parse_args, IWikiMacroProvider
from trac.wiki.macros import WikiMacroBase
from trac.wiki.model import WikiPage
from trac.wiki.web_ui import WikiModule

class NewPageMacro(WikiMacroBase):
    """A macro to add scrippets to a page. Usage:
    """
    implements(IWikiMacroProvider,ITemplateProvider)

    def expand_macro(self, formatter, name, content, args):
        data = parse_args(content)[1]
        self.log.debug("EXPAND ARGUMENTS: %s " % data)
        req = formatter.req
        template = Chrome(self.env).load_template('newpageform.html',method='xhtml')
        data = Chrome(self.env).populate_data(req, data)
        
        rendered_result = template.generate(**data)
        return rendered_result
    
    # ITemplateProvider methods
    def get_templates_dirs(self):
        from pkg_resources import resource_filename
        return [resource_filename('newpage', 'templates')]

    def get_htdocs_dirs(self):
        from pkg_resources import resource_filename
        return [('newpage', resource_filename(__name__, 'htdocs'))] 

