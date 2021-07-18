#! /bin/bash
echo "----Testing service 1-----"
cd service1/
pip3 install -r requirements.txt
python3 -m pytest --cov . --cov-report html

cd ..

echo "----Testing service 2-----"
cd service2/
pip3 install -r requirements.txt
python3 -m pytest --cov . --cov-report html

cd ..

echo "----Testing service 3-----"
cd service3/
pip3 install -r requirements.txt
python3 -m pytest --cov . --cov-report html

cd ..

echo "----Testing service 4-----"
cd service4/
pip3 install -r requirements.txt
python3 -m pytest --cov . --cov-report html

echo "----Testing completed----"