Summary:	Norwegian resources for SeaMonkey
Summary(pl):	Norweskie pliki jêzykowe dla SeaMonkeya
Name:		seamonkey-lang-nb
Version:	1.0
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/contrib-localized/seamonkey-%{version}.nb-NO.langpack.xpi
# Source0-md5:	935b8004f94a8febefdf78d6a022bb43
Source1:	http://www.mozilla-enigmail.org/downloads/lang/0.9x/enigmail-nb-NO-0.9x.xpi
# Source1-md5:	2aa5734f939734bdc05a29e0f2cf1c3e
Source2:	gen-installed-chrome.sh
URL:		http://www.mozilla.org/projects/seamonkey/
BuildRequires:	unzip
Requires(post,postun):	seamonkey >= %{version}
Requires(post,postun):	textutils
Requires:	seamonkey >= %{version}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_chromedir	%{_datadir}/seamonkey/chrome

%description
Norwegian resources for SeaMonkey.

%description -l pl
Norweskie pliki jêzykowe dla SeaMonkeya.

%prep
%setup -q -c -T
unzip %{SOURCE0}
unzip -o %{SOURCE1}
install %{SOURCE2} .
./gen-installed-chrome.sh locale bin/chrome/{NO,nb-NO,nb-unix}.jar \
	> lang-nb-installed-chrome.txt
./gen-installed-chrome.sh locale chrome/enigmail-nb-NO.jar \
	>> lang-nb-installed-chrome.txt

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}

install bin/chrome/{NO,nb-NO,nb-unix}.jar $RPM_BUILD_ROOT%{_chromedir}
install chrome/enigmail-nb-NO.jar $RPM_BUILD_ROOT%{_chromedir}
install lang-nb-installed-chrome.txt $RPM_BUILD_ROOT%{_chromedir}
cp -r bin/defaults $RPM_BUILD_ROOT%{_datadir}/seamonkey

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/seamonkey-chrome+xpcom-generate

%postun
%{_sbindir}/seamonkey-chrome+xpcom-generate

%files
%defattr(644,root,root,755)
%{_chromedir}/NO.jar
%{_chromedir}/nb-NO.jar
%{_chromedir}/nb-unix.jar
%{_chromedir}/enigmail-nb-NO.jar
%{_chromedir}/lang-nb-installed-chrome.txt
%{_datadir}/seamonkey/defaults/messenger/NO
%{_datadir}/seamonkey/defaults/profile/NO
