# _base_ = './danet_r50-d8_512x512_40k_voc12aug.py'
# model = dict(pretrained='open-mmlab://resnet101_v1c', backbone=dict(depth=101))

_base_ = [
    '../_base_/models/danet_r50-d8.py',   #这个是网络的骨架，使用单卡记得去骨架模型里将SyncBN改成BN
    '../_base_/datasets/my_dataset.py',   #换成自己定义的数据集
    '../_base_/default_runtime.py',
    '../_base_/schedules/schedule_20k.py'
]
model = dict(
    decode_head=dict(num_classes=2), auxiliary_head=dict(num_classes=2)) #换成自己的分类类别数