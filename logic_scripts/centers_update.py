import click
import numpy as np

@click.command("centers_update")
@click.option('--cluster', type=int, help='a num of cluster to process')
@click.option('--new_gen', help="a number of new data generation")
def centers_update(cluster, new_gen):
    cur_centers = np.load('/opt/clusters/centers.npy')
    new_centers = np.load(f'/storage/dgs/dg{new_gen}/centers.npy')[cluster, :]
    cur_centers[cluster, :] = new_centers
    np.save('/opt/clusters/centers', cur_centers)

if __name__ == '__main__':
    centers_update()