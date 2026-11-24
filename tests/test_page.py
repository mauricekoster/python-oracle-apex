from apexparser import *


def test_page_0(apex_parser):
    p = apex_parser.parse(
"""page A (
    )
""")

    assert isinstance(p, Page)

def test_page_1(apex_parser):
    p = apex_parser.parse(
"""page A (
        page: 1000
        name: Hallo
        alias: HOME
        title: How the West was won
    )
""")

    assert isinstance(p, Page)
    assert p.name == "Hallo"
    assert p.alias == "HOME"
    assert p.title == "How the West was won"


def test_page_appearance(apex_parser):
    p : Page = apex_parser.parse(
    """page A (
        name: Hallo

        appearance {
            pageMode: normal
            pageTemplate: @/standard
            dialogTemplate: @/dialog
            templateOptions: #DEFAULT#
            cssClasses: [
                aap
                noot
                mies
            ]
            mediaType: image
        }
    )
""")
    assert isinstance(p, Page)
    assert p.name == "Hallo"
    assert p.appearance.pageMode == 'normal'
    assert p.appearance.pageTemplate == '@/standard'
    assert p.appearance.dialogTemplate == '@/dialog'
    assert p.appearance.templateOptions == ['#DEFAULT#']
    assert p.appearance.cssClasses == ['aap', 'noot', 'mies']
    assert p.appearance.mediaType == 'image'


def test_page_navigation(apex_parser):
    p : Page = apex_parser.parse(
    """page A (
        name: Hallo

        navigation {
            cursorFocus: doNotFocusCursor
            warnOnUnsavedChanges: false
        }
    )
""")
    assert isinstance(p, Page)
    assert p.name == "Hallo"
    assert p.navigation.cursorFocus == "doNotFocusCursor"
    assert p.navigation.warnOnUnsavedChanges == False


def test_page_html_header(apex_parser):
    p : Page = apex_parser.parse(
    """page A (
        name: Hallo

        htmlHeader {
            htmlHeader:
                ```html
                <p></p>
                ```
            pageHtmlBodyAttribute:
                ```html
                <i></i>
                ```
        }
    )
""")
    assert isinstance(p, Page)
    assert p.name == "Hallo"
    assert p.htmlHeader.htmlHeader == "```html\n<p></p>\n```"
    assert p.htmlHeader.pageHtmlBodyAttribute == "```html\n<i></i>\n```"


def test_page_security(apex_parser):
    p : Page = apex_parser.parse(
    """page A (
        name: Hallo

        security {
            authorizationScheme: @auth
            authentication: required
            deepLinking: true
            pageAccessProtection: argumentsMustHaveChecksum
            formAutoComplete: false
            browserCache: true
        }
    )
""")
    assert isinstance(p, Page)
    assert p.name == "Hallo"
    assert p.security.authorizationScheme == "@auth"
    assert p.security.authentication == "required"
    assert p.security.deepLinking == True
    assert p.security.pageAccessProtection == "argumentsMustHaveChecksum"
    assert p.security.formAutoComplete == False
    assert p.security.browserCache == True


def test_page_help(apex_parser):
    p : Page = apex_parser.parse(
    """page A (
        name: Hallo

        help {
            helpText: No help is available for this page.
        }
    )
""")
    assert p.help.helpText == "No help is available for this page."


def test_page_advanced(apex_parser):
    p : Page = apex_parser.parse(
    """page A (
        name: Hallo

        advanced {
            enableMetaTags: true
            enableDuplicatePageSubmissions: false
            reloadOnSubmit: always
            duplicateSubmissionUrl: http://example.com
        }
    )
""")
    assert p.advanced.enableMetaTags == True
    assert p.advanced.enableDuplicatePageSubmissions == False
    assert p.advanced.reloadOnSubmit == "always"
    assert p.advanced.duplicateSubmissionUrl == "http://example.com"



def test_page_javascript(apex_parser):
    p : Page = apex_parser.parse(
    """page A (
        name: Hallo
        javaScript {
            fileUrls: [
                url1
                url2
            ]
            executeWhenPageLoads:
                ```js
                some code
                ```
            functionAndGlobalVariableDeclaration: var htmldb_delete_message = '"DELETE_CONFIRM_MSG"';
            includeStandardJavaScriptAndCss: true
        }
    )
""")

    assert isinstance(p, Page)
    assert p.javaScript.fileUrls == ['url1', 'url2']
    assert p.javaScript.executeWhenPageLoads == '```js\nsome code\n```'
    assert p.javaScript.functionAndGlobalVariableDeclaration == 'var htmldb_delete_message = \'"DELETE_CONFIRM_MSG"\';'
    assert p.javaScript.includeStandardJavaScriptAndCss == True