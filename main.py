from kivy.app import App
from kivy.uix.button import Button
from kivy.lang.builder import Builder
from kivymd.theming import ThemeManager
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock

from sympy.parsing.sympy_parser import parse_expr
from sympy import *
from kivymd.label import MDLabel
kvv="""

#:import Toolbar kivymd.toolbar.Toolbar
#:import ThemeManager kivymd.theming.ThemeManager
#:import MDNavigationDrawer kivymd.navigationdrawer.MDNavigationDrawer
#:import NavigationLayout kivymd.navigationdrawer.NavigationLayout
#:import NavigationDrawerDivider kivymd.navigationdrawer.NavigationDrawerDivider
#:import NavigationDrawerToolbar kivymd.navigationdrawer.NavigationDrawerToolbar
#:import NavigationDrawerSubheader kivymd.navigationdrawer.NavigationDrawerSubheader
#:import MDCheckbox kivymd.selectioncontrols.MDCheckbox
#:import MDSwitch kivymd.selectioncontrols.MDSwitch
#:import MDList kivymd.list.MDList
#:import OneLineListItem kivymd.list.OneLineListItem
#:import TwoLineListItem kivymd.list.TwoLineListItem
#:import ThreeLineListItem kivymd.list.ThreeLineListItem
#:import OneLineAvatarListItem kivymd.list.OneLineAvatarListItem
#:import OneLineIconListItem kivymd.list.OneLineIconListItem
#:import OneLineAvatarIconListItem kivymd.list.OneLineAvatarIconListItem
#:import MDTextField kivymd.textfields.MDTextField
#:import MDSpinner kivymd.spinner.MDSpinner
#:import MDCard kivymd.card.MDCard
#:import MDSeparator kivymd.card.MDSeparator
#:import MDDropdownMenu kivymd.menu.MDDropdownMenu
#:import get_color_from_hex kivy.utils.get_color_from_hex
#:import colors kivymd.color_definitions.colors
#:import SmartTile kivymd.grid.SmartTile
#:import MDSlider kivymd.slider.MDSlider
#:import MDTabbedPanel kivymd.tabs.MDTabbedPanel
#:import MDTab kivymd.tabs.MDTab
#:import MDProgressBar kivymd.progressbar.MDProgressBar
#:import MDAccordion kivymd.accordion.MDAccordion
#:import MDAccordionItem kivymd.accordion.MDAccordionItem
#:import MDAccordionSubItem kivymd.accordion.MDAccordionSubItem
#:import MDThemePicker kivymd.theme_picker.MDThemePicker
#:import MDBottomNavigation kivymd.tabs.MDBottomNavigation
#:import MDBottomNavigationItem kivymd.tabs.MDBottomNavigationItem


BoxLayout:
    orientation: 'vertical'
    MDLabel:
        id:out
        text:'0'
        size_hint_y:0.4
        font_style:'Title'
        font_size:40
        halign:'right'
        padding:(20,0)
    ScreenManager:
        id:screenmgr
        Screen:
            name: 'buttons'
            GridLayout:
                cols:3
                GridLayout:
                    cols:3
                    MDFlatButton:
                        size_hint:(1,1)
                        on_release:out.text+='1'
                        MDLabel:
                            text:'1'
                            font_size:20
                            halign:'center'
                    MDFlatButton:
                        on_release:out.text+='2'
                        size_hint:(1,1)
                        MDLabel:
                            text:'2'
                            font_size:20
                            halign:'center'
                    MDFlatButton:
                        on_release:out.text+='3'
                        size_hint:(1,1)
                        MDLabel:
                            text:'3'
                            font_size:20
                            halign:'center'
                    MDFlatButton:
                        on_release:out.text+='4'
                        size_hint:(1,1)
                        MDLabel:
                            text:'4'
                            font_size:20
                            halign:'center'
                    MDFlatButton:
                        on_release:out.text+='5'
                        size_hint:(1,1)
                        MDLabel:
                            text:'5'
                            font_size:20
                            halign:'center'
                    MDFlatButton:
                        on_release:out.text+='6'
                        size_hint:(1,1)
                        MDLabel:
                            text:'6'
                            font_size:20
                            halign:'center'
                    MDFlatButton:
                        on_release:out.text+='7'
                        size_hint:(1,1)
                        MDLabel:
                            text:'7'
                            font_size:20
                            halign:'center'
                    MDFlatButton:
                        on_release:out.text+='8'
                        size_hint:(1,1)
                        MDLabel:
                            text:'8'
                            font_size:20
                            halign:'center'
                    MDFlatButton:
                        on_release:out.text+='9'
                        size_hint:(1,1)
                        MDLabel:
                            text:'9'
                            font_size:20
                            halign:'center'
                    MDFlatButton:
                        on_release:out.text+='.'
                        size_hint:(1,1)
                        MDLabel:
                            text:'.'
                            font_size:20
                            halign:'center'
                    MDFlatButton:
                        on_release:out.text+='0'
                        size_hint:(1,1)
                        MDLabel:
                            text:'0'
                            font_size:20
                            halign:'center'
                    MDFlatButton:
                        id:equal_but
                        size_hint:(1,1)
                        MDLabel:
                            text:'='
                            font_size:20
                            halign:'center'

                GridLayout:
                    cols:1
                    size_hint_x:0.15
                    MDFlatButton:
                        size_hint:(1,1)
                        id:cancel_but
                        text:'DEL'

                    MDFlatButton:
                        size_hint:(1,1)
                        id:plus
                        text:'+'
                        on_release:out.text+='+'
                    MDFlatButton:
                        size_hint:(1,1)
                        id:minus
                        text:'-'
                        on_release:out.text+='-'
                    MDFlatButton:
                        size_hint:(1,1)
                        id:multiply
                        text:'x'
                        on_release:out.text+='*'
                    MDFlatButton:
                        size_hint:(1,1)
                        id:divide
                        text:'/'
                        on_release:out.text+='/'
                MDIconButton:
                    size_hint:(0.1,1)
                    icon:'arrow-right'
                    on_press:screenmgr.current='trigo'
        Screen:
            name:'trigo'

            GridLayout:
                cols:2
                MDIconButton:
                    size_hint:(0.1,1)
                    icon:'arrow-left'
                    on_press:screenmgr.current='buttons'
                
                GridLayout:
                    cols:3
                    MDFlatButton:
                        on_release:out.text+='sin('
                        size_hint:(1,1)
                        MDLabel:
                            text:'sin'
                            font_size:20
                            halign:'center'
                    MDFlatButton:
                        on_release:out.text+='cos('
                        size_hint:(1,1)
                        MDLabel:
                            text:'cos'
                            font_size:20
                            halign:'center'
                    MDFlatButton:
                        on_release:out.text+='tan('
                        size_hint:(1,1)
                        MDLabel:
                            text:'tan'
                            font_size:20
                            halign:'center'
                    MDFlatButton:
                        on_release:out.text+='('
                        size_hint:(1,1)
                        MDLabel:
                            text:'('
                            font_size:20
                            halign:'center'
                    MDFlatButton:
                        on_release:out.text+=')'
                        size_hint:(1,1)
                        MDLabel:
                            text:')'
                            font_size:20
                            halign:'center'
                    
                    

"""


class mainapp(BoxLayout):
    def __init__(self,**kwargs):
        BoxLayout.__init__(self,**kwargs)
        self.orientation='vertical'

        self.numpad=Builder.load_string(kvv)
        self.add_widget(self.numpad)

        #Buttons
        self.out=self.numpad.ids['out']
        self.delbutton=self.numpad.ids['cancel_but']
        self.equalbutton=self.numpad.ids['equal_but']
        #Binds
        self.delbutton.bind(on_release=self.delbut)
        self.equalbutton.bind(on_release=self.equalcall)
        #Clock
        Clock.schedule_interval(self.outputloop,0)

    def outputloop(self,dt):
        tex=self.out.text
        if tex=='':
            self.out.text='0'
        try:
            if int(tex)>0:
                self.out.text=str(int(tex))
        except:
            pass

    def delbut(self,ins):
        tex = self.out.text
        tex=tex[:-1]
        self.out.text=tex

    def equalcall(self,ins):
        try:
            expr=N(parse_expr(self.out.text,evaluate=True))
            tex=str(expr)
            self.out.text=tex
        except:
            pass

class myapp(App):
    theme_cls=ThemeManager()
    def build(self):
        return mainapp()


A=myapp()
A.run()