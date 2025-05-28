import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from src.utils.utils import dataset
import pandas as pd

class TestDataset:
    """Test cases for the dataset utility class."""
    
    def test_dataset_initialization(self):
        """Test that dataset can be initialized properly."""
        df = pd.DataFrame({'test': [1, 2, 3]})
        ds = dataset(name="test", dataset=df)
        
        assert ds.name == "test"
        assert len(ds.dataset) == 3
        assert ds.text_accuracy == 0.0
        
    def test_dataset_repr(self):
        """Test the string representation of dataset."""
        df = pd.DataFrame({'test': [1, 2, 3]})
        ds = dataset(name="test", dataset=df)
        
        repr_str = repr(ds)
        assert "test" in repr_str
        assert "size=3" in repr_str

def test_get_token_tokens():
    """Test token extraction functionality."""
    from src.utils.utils import get_token_tokens
    
    # Create test data
    test_df = pd.DataFrame({
        'Tokens': ['["B-NAME", "I-NAME", "O"]', '["B-EMAIL", "O", "O"]']
    })
    
    cleaned_tokens, raw_tokens = get_token_tokens(test_df)
    
    assert "NAME" in cleaned_tokens
    assert "EMAIL" in cleaned_tokens
    assert len(raw_tokens) >= 2