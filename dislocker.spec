%define major 0

Summary:	FUSE driver to read/write Windows' BitLocker-ed volumes under Linux / Mac OSX
Name:		dislocker
Version:	0.7.3
Release:	2
License:	GPLv2
Group:		System/Libraries
URL:		https://github.com/Aorimn/dislocker
Source0:	%{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:	cmake
BuildRequires:	mbedtls-devel
BuildRequires:	pkgconfig(fuse)

%description
This software has been designed to read BitLocker encrypted
partitions under a Linux system. The driver has the capability
to read/write on:

Windows Vista, 7, 8, 8.1 and 10 encrypted partitions - that's 
AES-CBC, AES-XTS, 128 or 256 bits, with or without the Elephant
diffuser, encrypted partitions;
BitLocker-To-Go encrypted partitions - that's USB/FAT32 partitions.

%libpackage %{name} %{major}

%prep
%autosetup -p1

%build
%cmake
%make_build

%install
%make_install -C build
rm -rf %{buildroot}%{_libdir}/libdislocker.so

%files
%doc README.md LICENSE.txt
%{_bindir}/%{name}*
%doc %{_mandir}/man1/*
