#!/bin/bash
# args:
# prev_gen
# new_gen
# cluster 
for host in kc1 kc2; do
    # убираем всё по текущему кластеру из Bind Mounted папок
    ssh $host "mv /opt/clusters/clust$3 /storage/dgs/dg$1/clust$3"
    # закидываем обновленный кластер в Bind Mounted папки
    rsync -a --progress --remove-source-files /storage/dgs/dg$2/clust$3 $host:/opt/clusters/
    # обновление центра кластера
    ssh $host "python3 ./logic_scripts/centers_update.py --cluster $3 --new_gen $2 "
done
# rolling update сервиса кластера и API gateway
ssh kc1 "docker service update --force --update-parallelism 1 --update-delay 20s --update-failure-action=rollback --update-max-failure-ratio 0 qaserv_index_service_$3"
ssh kc1 "docker service update --force --update-parallelism 1 --update-delay 20s --update-failure-action=rollback --update-max-failure-ratio 0 qaserv_gateway"
