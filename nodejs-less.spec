%{?nodejs_find_provides_and_requires}
Name:                nodejs-less
Version:             3.10.3
Release:             1
Summary:             Less.js The dynamic stylesheet language
License:             ASL 2.0 and BSD
URL:                 http://lesscss.org
Source0:             http://registry.npmjs.org/less/-/less-%{version}.tgz
Patch0:              nodejs-less-mime2.patch
BuildArch:           noarch
ExclusiveArch:       %{nodejs_arches} noarch aarch64 x86_64
BuildRequires:       nodejs-packaging
BuildRequires:       npm(clone) npm(image-size) npm(less-plugin-clean-css) npm(mime) npm(source-map)
Provides:            lessjs = %{version}-%{release}
Obsoletes:           lessjs < 1.3.3-2
%description
LESS extends CSS with dynamic behavior such as variables, mixins, operations
and functions. LESS runs on both the client-side (Chrome, Safari, Firefox)
and server-side, with Node.js and Rhino.

%prep
%autosetup -p 1 -n package
%nodejs_fixdep clone "^1.0.2"
%nodejs_fixdep --optional --remove errno
%nodejs_fixdep --optional --remove mkdirp
%nodejs_fixdep --optional image-size "^0.6.3"
%nodejs_fixdep --optional promise "^8.0.1"
%nodejs_fixdep --optional request "^2.67.0"
%nodejs_fixdep --optional source-map "^0.5.6"
rm -rf node_modules

%build

%check
%nodejs_symlink_deps --check --optional
rm test/less/import-module.less
rm test/css/3rd-party/*.css
rm test/less/3rd-party/*.less
%{__nodejs} test

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/less
cp -pr package.json index.js dist lib %{buildroot}/%{nodejs_sitelib}/less
mkdir -p %{buildroot}%{nodejs_sitelib}/less/bin
install -m755 -p bin/lessc %{buildroot}%{nodejs_sitelib}/less/bin
mkdir -p %{buildroot}%{_bindir}
ln -s %{nodejs_sitelib}/less/bin/lessc %{buildroot}%{_bindir}
%nodejs_symlink_deps

%files
%doc README.md CHANGELOG.md CONTRIBUTING.md
%license LICENSE
%{_bindir}/lessc
%{nodejs_sitelib}/less

%changelog
* Wed Aug 19 2020 zhanghua <zhanghua40@huawei.com> - 3.10.3-1
- Package init
