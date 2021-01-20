FROM tensorflow/tensorflow
RUN pip install Pillow tqdm pandas
COPY download.py /app/download.py
CMD ["python", "/app/download.py"]