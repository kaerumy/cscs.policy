from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='cscs.policy',
      version=version,
      description="",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author='',
      author_email='',
      url='http://svn.plone.org/svn/collective/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['cscs'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.app.dexterity',
          'plone.namedfile [blobs]',
          'collective.grok',
          'plone.app.referenceablebehavior',
          'cscs.theme',
          'cscs.content',
          'Products.CSCS',
          'plone.app.caching',
          'plone.app.theming',
          'Products.ContentWellPortlets',
          'Products.PloneKeywordManager',
          'collective.contentleadimage',
          'collective.plonetruegallery',
          'ftw.blog',
          'collective.quickupload',
          'collective.portlet.collectionmultiview',
          'Solgema.fullcalendar',
          'collective.prettyphoto',
          'wcc.carousel',
          'wildcard.media'
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
