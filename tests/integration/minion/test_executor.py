# -*- coding: utf-8 -*-

# Import python libs
from __future__ import absolute_import, print_function, unicode_literals

import logging

# Import Salt Testing libs
from tests.support.case import ModuleCase, ShellCase

log = logging.getLogger(__name__)


class ExecutorTest(ModuleCase, ShellCase):

    def setup(self):
        self.run_function('saltutil.sync_all')

    def test_executor(self):
        '''
        test that dunders are set
        '''
        data = self.run_call('test.arg --module-executors=arg')
        self.assertIn('test.arg fired', "".join(data))

    def test_executor_with_multijob(self):
        '''
        test that executor is fired when sending a multifunction job
        '''
        data = self.run_salt('\'*\' test.arg,test.arg foo,bar --module-executors=arg')
        self.assertIn('test.arg fired', "".join(data))

