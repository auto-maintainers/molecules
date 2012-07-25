# Use abs path, otherwise daily builds automagic won't work
%import /sabayon/molecules/spinbase-amazon-ami-ebs-image.common

# pre chroot command, example, for 32bit chroots on 64bit system, you always
# have to append "linux32" this is useful for inner_chroot_script
# prechroot:

# Path to source ISO file (MANDATORY)
source_iso: /sabayon/iso/Sabayon_Linux_SpinBase_DAILY_amd64.iso

release_version: 9
tar_name: Sabayon_Linux_SpinBase_9_amd64_Amazon_EBS_ext4_filesystem_image.tar.gz