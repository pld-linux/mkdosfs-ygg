Summary:	A program which creates MS-DOS FAT filesystems on Linux systems.
Name:		mkdosfs-ygg
Version:	0.3b
Release:	12
License:	GPL
Group:		Applications/System
Source:		ftp://ftp.yggdrasil.com/pub/dist/mkdosfs/%{name}-%{version}.tar.gz
Patch0:		%{name}-%{version}-fix.patch
Patch1:		%{name}-%{version}-sparc.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The mkdosfs program is used to create an MS-DOS FAT file system on a
Linux system device, usually a disk partition.

The mkdosfs package should be installed if your machine needs to support
MS-DOS style file systems.

%prep
%setup -q
%patch0 -p1 -b .fix
%patch1 -p1 -b .sparc

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/sbin
mkdir -p $RPM_BUILD_ROOT/usr/man/man8

install -m755 -s mkdosfs $RPM_BUILD_ROOT/sbin/mkfs.msdos
ln -sf mkfs.msdos $RPM_BUILD_ROOT/sbin/mkdosfs
install -m 644 mkdosfs.8 $RPM_BUILD_ROOT/usr/man/man8
ln -sf mkdosfs.8 $RPM_BUILD_ROOT/usr/man/man8/mkfs.msdos.8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/sbin/mkfs.msdos 
/sbin/mkdosfs
/usr/man/man8/mkfs.msdos.8
/usr/man/man8/mkdosfs.8
