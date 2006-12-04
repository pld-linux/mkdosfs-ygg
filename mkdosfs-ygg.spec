Summary:	A program which creates MS-DOS FAT filesystems on Linux systems
Summary(pl):	Program do tworzenia systemów plików MS-DOS FAT pod Linuksem
Name:		mkdosfs-ygg
Version:	0.3b
Release:	13
License:	GPL
Group:		Applications/System
Source0:	ftp://ftp.yggdrasil.com/pub/dist/mkdosfs/%{name}-%{version}.tar.gz
# Source0-md5:	32b5ba7975ae2236e631a22a1e123e1b
Patch0:		%{name}-%{version}-fix.patch
Patch1:		%{name}-%{version}-sparc.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin

%description
The mkdosfs program is used to create an MS-DOS FAT file system on a
Linux system device, usually a disk partition.

The mkdosfs package should be installed if your machine needs to
support MS-DOS style file systems.

%description -l pl
Program mkdosfs s³u¿y do tworzenia systemów plików MS-DOS FAT na
urz±dzeniach (zwykle partycjach).

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}

install mkdosfs $RPM_BUILD_ROOT%{_sbindir}/mkfs.msdos
ln -sf mkfs.msdos $RPM_BUILD_ROOT%{_sbindir}/mkdosfs
install mkdosfs.8 $RPM_BUILD_ROOT%{_mandir}/man8
echo '.so mkdosfs.8' > $RPM_BUILD_ROOT%{_mandir}/man8/mkfs.msdos.8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_sbindir}/mkfs.msdos
%attr(755,root,root) %{_sbindir}/mkdosfs
%{_mandir}/man8/mkfs.msdos.8*
%{_mandir}/man8/mkdosfs.8*
