#!/bin/bash

for host in kc1 kc2; do
    rsync -avz dgs $host:/storage/
done


