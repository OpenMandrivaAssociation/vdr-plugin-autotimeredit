
%define plugin	autotimeredit
%define name	vdr-plugin-%plugin
%define version	0.1.8
%define rel	12

Summary:	VDR plugin: OSD autotimer edit
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://www.fast-info.de/vdr/autotimeredit/
Source:		http://www.fast-info.de/vdr/autotimeredit/vdr-%plugin-%version.tar.bz2
Patch1:		http://gentoo.fh-luh.de/files/vdr-autotimeredit/autotimeredit-0.1.8.patch
BuildRequires:	vdr-devel >= 1.4.1-6
Requires:	vdr-abi = %vdr_abi

%description
This is a plugin for the Video Disk Recorder (VDR) to edit the vdradmind.at
for vdradmind via VDR on-screen-display (OSD).

%prep
%setup -q -n %plugin-%version
%patch1 -p4 -b .uint

# this plugin has somewhat bloated configuration scheme...

%vdr_plugin_params_begin %plugin
# Note that most of these options can also be set from the OSD setup menu and
# autotimeredit.conf.
# Read the documentation for more info.
#
# Autotimer-file (same for vdradmind!)
var=AUTOTIMER_FILE
param="-f AUTOTIMER_FILE"
default=%{_localstatedir}/vdradmin/vdradmind.at
# Hide the file from setup-menu
var=HIDE_AUTOTIMER_FILE
param="--ns_autotimerfile"
# Use SIGHUP (vdradmind) for update Autotimer
var=USE_SIGHUP_VDRADMIN
param=-p
default=yes
# Use SIGHUP (xxv) for update Autotimer
var=USE_SIGHUP_XXV
param=-x
# Hide the use_sgihup from setup-menu
var=HIDE_USE_SIGHUP
param=--ns_update_method
# Script/Config-file for force update autotimer
var=FORCE_UPDATE_FILE
param="-u FORCE_UPDATE_FILE"
default=%{_localstatedir}/vdradmin/vdradmind.conf
# Hide the vdradminupdate-file form setup-menu
var=HIDE_FORCE_UPDATE_FILE
param="--ns_vdradminupdate"
# Show the plugin in the mainmenu
var=VISIBLE
param=-m
# Hide the plugin in the mainmenu
var=HIDDEN
param=-M
# Select Name for entry in the mainmenu
var=MAINMENU_NAME
param="-n MAINMENU_NAME"
# Enable more logging
var=ENABLE_VERBOSE
param=-v
# Disable more logging
var=DISABLE_VERBOSE
param=-V
# Use the repeat feature from vdradmin bp0.9
var=USE_REPEAT
param=-r
# not use, it set automatic to use, if the autotimerfile with 11 values
var=NOT_USE_REPEAT
param=-R
# Hide the option from setup-menu
var=HIDE_USE_REPEAT
param=--ns_repeat_feature
# Use weekday feature (sets also USE_REPEAT)
var=USE_WEEKDAY
param=-k
default=yes
# not use, it set automatic to use, if the autotimerfile with 12 values
var=NOT_USE_WEEKDAY
param=-K
# Hide the option from setup-menu
var=HIDE_USE_WEEKDAY
param=--ns_weekday_feature
# Show the manual update line at begin of autotimer-list
var=UPDATE_BEGIN
param=-b
# Hide the manual update line at begin of autotimer-list
var=NO_UPDATE_BEGIN
param=-B
# Show the manual update line at end of autotimer-list
var=UPDATE_END
param=-e
# Hide the manual update line at end of autotimer-list
var=NO_UPDATE_END
param=-E
# When one or more Autotimer are modifed, by quit the plugin appears
# a question for force search update
var=QUESTION_UPDATE
param=-q
# Above but no question
var=NO_QUESTION_UPDATE
param=-Q
# For the Autotimerlist show search in title, subtitle and
# description as a single char
var=SHOW_FLAGS
param=-l
# Column is hidden
var=HIDE_FLAGS
param=-L
# For the Autotimerlist show the startsearchtime
var=SHOW_START
param=-a
# Column is hidden
var=HIDE_START
param=-A
# For the Autotimerlist show the stopsearchtime
var=SHOW_STOP
param=-t
# Column is hidden
var=HIDE_STOP
param=-T
# For the Autotimerlist show the searchchannel
var=SHOW_CHANNEL
param=-c
# Column is hidden
var=HIDE_CHANNEL
param=-C
# if show_channel the name of channel is use
var=SHOW_CHANNEL_NAME
param=-s
# if show_channel the number of channel is use
var=SHOW_CHANNEL_NUMBER
param=-S
# Hide the Preferr Command Line Parameter form setup-menu
var=HIDE_COMMANDLINE
param=--ns_commandline
# set the default choise for the dictionary (space '_', any special
# char with #xx) a dictionary for blacklist starts with '~' include
# subdictionary with '~~'
# example: "/some/dir,/another/dir"
var=DEFAULTDICTIONARY
param="-d DEFAULTDICTIONARY"
# Select the source for the defaultdictionary
# 0x01 - autotimer 0x02 - timer 0x04 - records 0x08 - commandline 0x10 - setup
var=USE_DEFAULTDICTIONARY
param="-D USE_DEFAULTDICTIONARY"
# Hide all options with default dictionary from setup-menu
var=HIDE_DEFAULTDICTIONARY
param=--ns_defaultdictionary
# time (hours) between two updates for defaultdictionary from
# records (-1 only by start, 0 by each call autotimeredit)
var=UPDATETIMERECORDS
param="-y UPDATETIMERECORDS"
# Hide the updatetimerecords option from setup-menu
var=HIDE_UPDATETIMERECORDS
param=--ns_updatetimerecords
# file for read more options (relativ to <config-dir>/plugins, or
# when begins with '/' absolute)
var=MORE_OPTIONS_FILE
param="@MORE_OPTIONS_FILE"
%vdr_plugin_params_end

%build
%vdr_plugin_build

%install
rm -rf %{buildroot}
%vdr_plugin_install

%clean
rm -rf %{buildroot}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY


