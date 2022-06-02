import pytest
from app.8_kth_missing import kth_missing_positive_number

def test_kth_missing_positive_number_finds_num_before_entire_given_list(self):
      # Arrange
      list = [2,3,4,7,11]
      k = 1

      # Act
      answer = kth_missing_positive_number(list, k)

      # Assert
      assert 1 == answer

  def test_kth_missing_number_finds_num_near_end_of_list(self):
      # Arrange
      list = [2,3,4,7,11]
      k = 5

      # Act
      answer = kth_missing_positive_number(list, k)
      
      # Assert
      assert 9 == answer

  def test_kth_missing_positive_number_finds_num_after_entire_given_list(self):
      # Arrange
      list = [1,2,3,4]
      k = 2

      # Act
      answer = kth_missing_positive_number(list, k)
      
      # Assert
      assert 6 == answer

  def test_kth_missing_positive_number_2nd_number_before_list_starts(self):
      # Arrange
      list = [3,4,5,7,11]
      k = 2

      # Act
      answer = kth_missing_positive_number(list, k)
      
      assert 2 == answer
