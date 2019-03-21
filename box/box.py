"""A simple XBlock for displaying content in coloured boxes"""

import pkg_resources

from xblock.core import XBlock
from xblock.fields import Scope, String
from xblock.fragment import Fragment
from xblockutils.studio_editable import StudioEditableXBlockMixin

# class ShowSize(object):
#     """
#     Constants for when to show server
#     """
#     dwidth = "800px"
#     dlenth = "600px"

class BoxXBlock(StudioEditableXBlockMixin, XBlock):
    display_name = String(display_name="Display name", default='External Html', scope=Scope.settings ,
                          values=('Live Programming', 'Visualize Coding', 'Lab', 'External Html'))
    # boxcolour = String(display_name="Box Colour", values=('Grey', 'Red', 'Green', 'Blue', 'Yellow'),
    #     default="Grey", scope=Scope.settings,
    #     help="Pick a colour for your box.")
    boxwidth = String(display_name="Box width",
                      scope=Scope.settings,
                      help="Width for your box.",
                      default="100%",
                      )
    boxheight = String(display_name="Box height",
                      scope=Scope.settings,
                      help="Height for your box.",
                      default="800px",
                      )
    boxurl = String(display_name="Box url",
                       scope=Scope.settings,
                       help="url for your box.",
                       default=u"https://codetutor.openedu.tw/index.html",
                       )
    # boxcontent = String(display_name="Contents", multiline_editor='html', resettable_editor=False,
    #     default="", scope=Scope.content,
    #     help="Enter content to be displayed within your box")



    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    def student_view(self, context=None):
        """
        The primary view of the BoxXBlock, shown to students
        when viewing courses.
        """

        html = self.resource_string("static/html/box.html")
        frag = Fragment(html.format(self=self))
        frag.add_css(self.resource_string("static/css/box.css"))
        frag.add_javascript(self.resource_string("static/js/src/box.js"))
        frag.initialize_js('BoxXBlock')
        return frag
    # Make fields editable in studio
    # editable_fields = ('display_name', 'boxcolour', 'boxwidth', 'boxcontent', )
    editable_fields = ('display_name', 'boxwidth', 'boxheight', 'boxurl')


