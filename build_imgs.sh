#!/bin/bash
echo "Giving executable rights to scripts"

chmod +x ./template_img/build_template.sh
chmod +x ./serving_img/build_serving.sh
chmod +x ./api_img/build_api.sh

echo "Begining to build images"

echo "Template image"
./template_img/build_template.sh
echo "Template done"

echo "Serving image"
./serving_img/build_serving.sh
echo "Serving done"

echo "API image"
./api_img/build_api.sh
echo "API done"

echo "Success!"