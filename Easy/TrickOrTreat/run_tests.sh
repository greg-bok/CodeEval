python -m unittest unit_tests
python trick_or_treat.py data.txt > results.txt
diff results.txt expected.txt
rm results.txt

