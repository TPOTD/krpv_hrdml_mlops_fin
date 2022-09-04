FROM 65.108.82.162:8090/template
WORKDIR /workspace
ADD . .
RUN chmod -R a+w /workspace
EXPOSE 5555

CMD ["flask", "run", "--host=0.0.0.0", "--port=5555"]