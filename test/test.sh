
# - Copy sample.py.template to sample.py

cp sample.py.template sample.py

# - Print sample.py before formatting

echo "Contents of sample.py before formatting:"
cat sample.py
echo "\n"

# - Run stepwise_code on sample.py

cd ../
python -m stepwise_code test/sample.py
cd test

# - Print sample.py after formatting

echo "Contents of sample.py after formatting:"
cat sample.py

# - Remove sample.py

rm sample.py