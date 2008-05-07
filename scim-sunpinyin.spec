%define snapdate 20070507

Name:		scim-sunpinyin
Summary:	SLM (Statistical Language Model) based IME
Version:	1.0
Release:	%mkrel -c %snapdate 1
Group:		System/Internationalization
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
License:	CDDL and LGPLv2+
URL:		http://www.opensolaris.org/os/project/input-method/
# fwang: the tarball is generated by:
# hg clone ssh://anon@hg.opensolaris.org/hg/nv-g11n/inputmethod
# cd inputmethod
# hg archive -t tbz2 scim-sunpinyin.tar.bz2
Source0:	%{name}.tar.bz2
Requires:		scim-client = %{scim_api}
BuildRequires:		scim-devel >= 1.4.7

%description
SunPinyin (developed by Sun Asian G11N Center, shipped since Solaris 10,
and opensource'd on OS.o) is a SLM (Statistical Language Model) based IME.

This packagae contains SunPinyin's scim wrapper.

%prep
%setup -q -n %name/sunpinyin/ime

%build
./autogen.sh
%configure2_5x --disable-cle --enable-scim
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

# remove unneeded files
rm -f %{buildroot}/%scim_plugins_dir/*/*.{a,la}

%find_lang sunpinyin

%clean
rm -rf $RPM_BUILD_ROOT

%files -f sunpinyin.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%{scim_plugins_dir}/*/*.so
%{_datadir}/scim/icons/*
%{_datadir}/scim/sunpinyin
