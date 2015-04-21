# TODO:
# - split into separate cn/jp/kr/otc/tw subpackages
Summary:	Adobe Source HanSans
Name:		fonts-OTF-Adobe-SourceHanSans
Version:	1.002
Release:	1
License:	OFL v1.1
Group:		Fonts
Source0:	https://github.com/adobe-fonts/source-han-sans/archive/1.002R.tar.gz
# Source0-md5:	6b7f44a2e15f585a3ff5eff7754edb32
Source1:	44-source-han-sans-cn.conf
Source2:	44-source-han-sans-jp.conf
Source3:	44-source-han-sans-kr.conf
Source4:	44-source-han-sans-otc.conf
Source5:	44-source-han-sans-tw.conf
URL:		https://github.com/adobe-fonts/source-han-sans
BuildRequires:	unzip
Requires(post,postun):	fontpostinst
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         otffontsdir     %{_fontsdir}/OTF

%description
Source Han Sans is a set of OpenType/CFF Pan-CJK fonts.

%prep
%setup -q -n source-han-sans-%{version}R

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{otffontsdir},%{_datadir}/fontconfig/conf.avail,%{_sysconfdir}/fonts/conf.d}

find . -type f -name '*.otf' -exec install -vp "{}" "$RPM_BUILD_ROOT%{otffontsdir}" ";"

install -p %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/fontconfig/conf.avail/44-source-han-sans-cn.conf
install -p %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/fontconfig/conf.avail/44-source-han-sans-jp.conf
install -p %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/fontconfig/conf.avail/44-source-han-sans-kr.conf
install -p %{SOURCE4} $RPM_BUILD_ROOT%{_datadir}/fontconfig/conf.avail/44-source-han-sans-otc.conf
install -p %{SOURCE5} $RPM_BUILD_ROOT%{_datadir}/fontconfig/conf.avail/44-source-han-sans-tw.conf
ln -s %{_datadir}/fontconfig/conf.avail/44-source-han-sans-cn.conf $RPM_BUILD_ROOT%{_sysconfdir}/fonts/conf.d/
ln -s %{_datadir}/fontconfig/conf.avail/44-source-han-sans-jp.conf $RPM_BUILD_ROOT%{_sysconfdir}/fonts/conf.d/
ln -s %{_datadir}/fontconfig/conf.avail/44-source-han-sans-kr.conf $RPM_BUILD_ROOT%{_sysconfdir}/fonts/conf.d/
ln -s %{_datadir}/fontconfig/conf.avail/44-source-han-sans-otc.conf $RPM_BUILD_ROOT%{_sysconfdir}/fonts/conf.d/
ln -s %{_datadir}/fontconfig/conf.avail/44-source-han-sans-tw.conf $RPM_BUILD_ROOT%{_sysconfdir}/fonts/conf.d/

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst OTF

%postun
fontpostinst OTF

%files
%defattr(644,root,root,755)
%doc LICENSE.txt README.md
%{otffontsdir}/SourceHanSans*.otf
%{_sysconfdir}/fonts/conf.d/44-source-han-sans-cn.conf
%{_sysconfdir}/fonts/conf.d/44-source-han-sans-jp.conf
%{_sysconfdir}/fonts/conf.d/44-source-han-sans-kr.conf
%{_sysconfdir}/fonts/conf.d/44-source-han-sans-otc.conf
%{_sysconfdir}/fonts/conf.d/44-source-han-sans-tw.conf
%{_datadir}/fontconfig/conf.avail/44-source-han-sans-cn.conf
%{_datadir}/fontconfig/conf.avail/44-source-han-sans-jp.conf
%{_datadir}/fontconfig/conf.avail/44-source-han-sans-kr.conf
%{_datadir}/fontconfig/conf.avail/44-source-han-sans-otc.conf
%{_datadir}/fontconfig/conf.avail/44-source-han-sans-tw.conf
