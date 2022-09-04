FROM 65.108.82.162:8090/template
WORKDIR /workspace
ADD . .
RUN chmod -R a+w /workspace
EXPOSE 5105
CMD  ["flask", "run", "-h", "0.0.0.0", "-p", "5105"]