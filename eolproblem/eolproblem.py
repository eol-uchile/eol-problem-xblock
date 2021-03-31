from web_fragments.fragment import Fragment
from pkg_resources import resource_string

from xmodule.util.xmodule_django import add_webpack_to_fragment
from xmodule.x_module import shim_xmodule_js
from xmodule.capa_module import ProblemBlock

from xblockutils.resources import ResourceLoader

loader = ResourceLoader(__name__)
# Make '_' a no-op so we can scrape strings
_ = lambda text: text

class EolProblemXBlock(ProblemBlock):

    mako_template = "templates/eolproblem/problem-edit.html"

    def studio_view(self, _context):
        """
            (Override) Return the studio view.
            ProblemBlock original render_template not working with custom mako templates
                fragment = Fragment(self.system.render_template(self.mako_template, self.get_context()))
        """
        template = loader.render_mako_template(self.mako_template, self.get_context())
        fragment = Fragment(template)
        add_webpack_to_fragment(fragment, 'ProblemBlockStudio')
        shim_xmodule_js(fragment, 'MarkdownEditingDescriptor')
        return fragment