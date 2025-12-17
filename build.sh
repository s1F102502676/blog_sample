set -o errexit

pip install -r requirements.txt

python manage.py colllection --no-input

python manage.py migrate