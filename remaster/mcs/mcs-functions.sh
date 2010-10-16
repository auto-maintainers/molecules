#!/bin/bash

_is_live() {
	cdroot=$(cat /proc/cmdline | grep cdroot)
	if [ -n "${cdroot}" ]; then
		return 0
	else
		return 1
	fi
}

_setup_fds_live() {
	# setup 389-ds
	tmp_config_file="$(mktemp)"
	echo "[General]
FullMachineName=sabayon
SuiteSpotUserID=dirsrv
SuiteSpotGroup=dirsrv
ConfigDirectoryAdminPwd=mcsmanager
AdminDomain=sabayon

[slapd]
ServerPort=389
ServerIdentifier=sabayon
Suffix=dc=babel,dc=it
RootDN=cn=Directory Manager
RootDNPwd=mcsmanager

[admin]
Port=9830
SysUser=dirsrv
ServerIpAddress=127.0.0.1
ServerAdminID=admin
ServerAdminPwd=mcsmanager
" > "${tmp_config_file}"
	# FIXME: calling the script directly, from init, won't work, WTF!
	su - -c "/usr/sbin/setup-ds-admin.pl -f ${tmp_config_file} --silent" || return 1
	echo "389 Directory Server configured."
	return 0
}

FDS_SETUP_FILE="/etc/.389-sabayon-configured"

_setup_fds_installed() {
	if [ -e "${FDS_SETUP_FILE}" ]; then
		return
	fi
	# First, setup 389
	_setup_fds_live
	# then make it autostart at the next boot
	rc-update add 389-ds default
	rc-update add 389-admin default
	# do the whole thing once
	touch "${FDS_SETUP_FILE}"
}


setup_fds() {
	# setup 389
	( _is_live && _setup_fds_live ) || _setup_fds_installed
}
