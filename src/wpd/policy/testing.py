from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting
from plone.app.testing import applyProfile

from zope.configuration import xmlconfig

class WpdPolicy(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        # Load ZCML for this package
        import wpd.policy
        xmlconfig.file('configure.zcml',
                       wpd.policy,
                       context=configurationContext)


    def setUpPloneSite(self, portal):
        applyProfile(portal, 'wpd.policy:default')

WPD_POLICY_FIXTURE = WpdPolicy()
WPD_POLICY_INTEGRATION_TESTING = \
    IntegrationTesting(bases=(WPD_POLICY_FIXTURE, ),
                       name="WpdPolicy:Integration")