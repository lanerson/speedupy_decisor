import unittest, os, sys
from unittest.mock import patch

project_folder = os.path.realpath(__file__).split('test/')[0]
sys.path.append(project_folder)

from execute_exp.services.revalidations.AbstractRevalidation import AbstractRevalidation
from execute_exp.entitites.FunctionCallProv import FunctionCallProv

class TestAbstractRevalidation(unittest.TestCase):
    def setUp(self):
        self.abstractRevalidation = AbstractRevalidation()
        self.get_function_call_prov_entry_namespace = 'execute_exp.services.revalidations.AbstractRevalidation.DataAccess.get_function_call_prov_entry'
        self.create_or_update_function_call_prov_entry_namespace = 'execute_exp.services.revalidations.AbstractRevalidation.DataAccess.create_or_update_function_call_prov_entry'
        self.fc_prov = FunctionCallProv('', {})
    
    def test_revalidation_in_current_execution_when_revalidation_will_occur(self):
        self.fc_prov.next_revalidation = 0
        reval_exec = self.abstractRevalidation.revalidation_in_current_execution(self.fc_prov)
        self.assertTrue(reval_exec)
    
    def test_revalidation_in_current_execution_when_revalidation_will_not_occur(self):
        self.fc_prov.next_revalidation = 3
        reval_exec = self.abstractRevalidation.revalidation_in_current_execution(self.fc_prov)
        self.assertFalse(reval_exec)
    
    def test_decrement_num_exec_to_next_revalidation_when_common_decrement(self):
        self.fc_prov.next_revalidation = 3
        with patch(self.create_or_update_function_call_prov_entry_namespace) as create_or_update_function_call_prov_entry:
            self.abstractRevalidation.decrement_num_exec_to_next_revalidation(self.fc_prov)
            create_or_update_function_call_prov_entry.assert_called_once()
            self.assertEqual(self.fc_prov.next_revalidation, 2)

    def test_decrement_num_exec_to_next_revalidation_when_decrement_to_0(self):
        self.fc_prov.next_revalidation = 1
        with patch(self.create_or_update_function_call_prov_entry_namespace) as create_or_update_function_call_prov_entry:
            self.abstractRevalidation.decrement_num_exec_to_next_revalidation(self.fc_prov)
            create_or_update_function_call_prov_entry.assert_called_once()
            self.assertEqual(self.fc_prov.next_revalidation, 0)
    
    def test_set_next_revalidation_with_greater_number_without_force(self):
        self.fc_prov.next_revalidation = 3
        with patch(self.create_or_update_function_call_prov_entry_namespace) as create_or_update_function_call_prov_entry:
            self.abstractRevalidation.set_next_revalidation(10, self.fc_prov, force=False)
            create_or_update_function_call_prov_entry.assert_not_called()
            self.assertEqual(self.fc_prov.next_revalidation, 3)

    def test_set_next_revalidation_with_lower_number_without_force(self):
        self.fc_prov.next_revalidation = 9
        with patch(self.create_or_update_function_call_prov_entry_namespace) as create_or_update_function_call_prov_entry:
            self.abstractRevalidation.set_next_revalidation(2, self.fc_prov, force=False)
            create_or_update_function_call_prov_entry.assert_called_once()
            self.assertEqual(self.fc_prov.next_revalidation, 2)

    def test_set_next_revalidation_with_equal_number(self):
        self.fc_prov.next_revalidation = 6
        with patch(self.create_or_update_function_call_prov_entry_namespace) as create_or_update_function_call_prov_entry:
            self.abstractRevalidation.set_next_revalidation(6, self.fc_prov, force=False)
            create_or_update_function_call_prov_entry.assert_not_called()
            self.assertEqual(self.fc_prov.next_revalidation, 6)

    def test_set_next_revalidation_with_greater_number_with_force(self):
        self.fc_prov.next_revalidation = 6
        with patch(self.create_or_update_function_call_prov_entry_namespace) as create_or_update_function_call_prov_entry:
            self.abstractRevalidation.set_next_revalidation(12, self.fc_prov, force=True)
            create_or_update_function_call_prov_entry.assert_called_once()
            self.assertEqual(self.fc_prov.next_revalidation, 12)

    def test_set_next_revalidation_with_lower_number_with_force(self):
        self.fc_prov.next_revalidation = 6
        with patch(self.create_or_update_function_call_prov_entry_namespace) as create_or_update_function_call_prov_entry:
            self.abstractRevalidation.set_next_revalidation(2, self.fc_prov, force=True)
            create_or_update_function_call_prov_entry.assert_called_once()
            self.assertEqual(self.fc_prov.next_revalidation, 2)
    
if __name__ == '__main__':
    unittest.main()