python -m unittest tests
echo ""
echo ""
echo "==========================================="
echo "running from console and diffing output...."
python compare_points.py data.txt > results.txt
diff -y expected.txt results.txt
rm results.txt
