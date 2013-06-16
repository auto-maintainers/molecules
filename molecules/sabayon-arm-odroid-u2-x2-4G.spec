%env %import ${SABAYON_MOLECULE_HOME:-/sabayon}/molecules/armv7-base.common
%env %import ${SABAYON_MOLECULE_HOME:-/sabayon}/molecules/odroid.common

# Release desc (the actual release description)
release_desc: armv7l Odroid U2/X2

# Release Version (used to generate release_file)
%env release_version: ${SABAYON_RELEASE:-11}

# Specify image file name (image file name will be automatically
# produced otherwise)
%env image_name: Sabayon_Linux_${SABAYON_RELEASE:-11}_armv7l_Odroid_U2_X2_4GB.img

# Specify the image file size in Megabytes. This is mandatory.
# To avoid runtime failure, make sure the image is large enough to fit your
# chroot data.
image_mb: 3800

# Path to boot partition data (MLO, u-boot.img etc)
%env source_boot_directory: ${SABAYON_MOLECULE_HOME:-/sabayon}/boot/arm/odroid-u2-x2

# External script that will generate the image file.
# The same can be copied onto a MMC by using dd
%env image_generator_script: ${SABAYON_MOLECULE_HOME:-/sabayon}/scripts/odroid_u2_x2_image_generator_script.sh
