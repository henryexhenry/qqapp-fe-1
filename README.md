# QQAPP

## dev

```bash
source ./venv/bin/activate
pip install -r requirements.txt
streamlit run webapp.py
```

## update service

```bash
swagger-codegen generate -i swagger.json -l python -o service
```

## ref

https://fullcalendar.io/docs#toc