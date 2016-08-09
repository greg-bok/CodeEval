python -m unittest unit_test
python longest_lines.py data.txt > results.txt
diff expected.txt results.txt
rm results.txt
cp -f longest_lines.py longest_lines.py2
