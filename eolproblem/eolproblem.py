
import pkg_resources
from xblock.core import XBlock
from xblock.fields import String, Scope
from xblock.fragment import Fragment

from xblockutils.studio_editable import StudioEditableXBlockMixin

# Make '_' a no-op so we can scrape strings
_ = lambda text: text

class EolProblemXBlock(StudioEditableXBlockMixin, XBlock):

    display_name = String(
        display_name=_("Display Name"),
        help=_("Display name for this module"),
        default="Constructor de Problemas Interactivo",
        scope=Scope.settings,
    )

    icon_class = "problem"
    editable_fields = ('display_name',)

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    def student_view(self, context=None):
        html = self.resource_string("static/html/eolproblem.html")
        frag = Fragment(html.format(xblock=self))
        frag.add_css(self.resource_string("static/css/eolproblem.css"))
        frag.add_javascript(self.resource_string("static/js/src/eolproblem.js"))
        frag.initialize_js('EolProblemXBlock')
        return frag