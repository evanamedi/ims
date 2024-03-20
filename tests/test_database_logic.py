import unittest
from unittest.mock import patch, MagicMock
from logic.database_logic import Table

class TestTable(unittest.TestCase):
    @patch('database_logic.db_cursor')
    @patch('database_logic.logger')
    
    def save_test_to_db(self, mock_logger, mock_db_cursor):
        
        mock_cursor = MagicMock()
        mock_db_cursor.return_value.__enter__.return_value = mock_cursor
        table = Table('test_table', id=1, name='Test')
        
        table.save_to_db()
        
        mock_cursor.execute.assert_called_once()
        mock_logger.info.assert_called_once_with('Added Successfully')

if __name__ == "__main__":
    unittest.main()
