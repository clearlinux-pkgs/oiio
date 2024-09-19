#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v18
# autospec commit: f35655a
#
Name     : oiio
Version  : 2.5.15.0
Release  : 61
URL      : https://github.com/OpenImageIO/oiio/archive/v2.5.15.0/oiio-2.5.15.0.tar.gz
Source0  : https://github.com/OpenImageIO/oiio/archive/v2.5.15.0/oiio-2.5.15.0.tar.gz
Summary  : OpenImageIO is a library for reading and writing images.
Group    : Development/Tools
License  : Apache-2.0
BuildRequires : Imath-dev
BuildRequires : LibRaw-dev
BuildRequires : OpenColorIO-data
BuildRequires : OpenColorIO-dev
BuildRequires : boost-dev
BuildRequires : buildreq-cmake
BuildRequires : bzip2-dev
BuildRequires : extra-cmake-modules pkgconfig(OpenEXR)
BuildRequires : fmt-dev
BuildRequires : freetype-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : libjpeg-turbo-staticdev
BuildRequires : libwebp-dev
BuildRequires : mesa-dev
BuildRequires : opencv-dev
BuildRequires : openexr-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(Qt6Core)
BuildRequires : pkgconfig(Qt6Gui)
BuildRequires : pkgconfig(libavutil)
BuildRequires : pkgconfig(libpng)
BuildRequires : pkgconfig(libraw)
BuildRequires : pkgconfig(libraw_r)
BuildRequires : pkgconfig(libswscale)
BuildRequires : pugixml-dev
BuildRequires : python3-dev
BuildRequires : robin-map-dev
BuildRequires : tiff-dev
BuildRequires : zlib-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<p align="center">
<img src="ASWF/logos/openimageio-horizontal-gradient.png">
</p>

%prep
%setup -q -n OpenImageIO-2.5.15.0
cd %{_builddir}/OpenImageIO-2.5.15.0
pushd ..
cp -a OpenImageIO-2.5.15.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1725466894
unset LD_AS_NEEDED
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake .. -Wno-dev \
-DBUILDSTATIC:BOOL=OFF \
-DBUILD_MISSING_FMT:BOOL=OFF \
-DCMAKE_DL_LIBS=dl \
-DCMAKE_INSTALL_DOCDIR:PATH=/usr/share/doc/oiio \
-DCMAKE_INSTALL_MANDIR:PATH=/usr/share/man/man1 \
-DCMAKE_SKIP_RPATH:BOOL=ON \
-DILMBASE_INCLUDE_PATH=/usr/include/OpenEXR \
-DINSTALL_DOCS:BOOL=ON \
-DINSTALL_FONTS:BOOL=ON \
-DLINKSTATIC:BOOL=OFF \
-DOpenGL_GL_PREFERENCE=GLVND \
-DSTOP_ON_WARNING=OFF \
-DUSE_EXTERNAL_PUGIXML:BOOL=ON \
-DUSE_FFMPEG:BOOL=OFF \
-DUSE_OPENCV:BOOL=ON \
-DUSE_OPENSSL:BOOL=ON \
-DUSE_PYTHON:BOOL=OFF  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake .. -Wno-dev \
-DBUILDSTATIC:BOOL=OFF \
-DBUILD_MISSING_FMT:BOOL=OFF \
-DCMAKE_DL_LIBS=dl \
-DCMAKE_INSTALL_DOCDIR:PATH=/usr/share/doc/oiio \
-DCMAKE_INSTALL_MANDIR:PATH=/usr/share/man/man1 \
-DCMAKE_SKIP_RPATH:BOOL=ON \
-DILMBASE_INCLUDE_PATH=/usr/include/OpenEXR \
-DINSTALL_DOCS:BOOL=ON \
-DINSTALL_FONTS:BOOL=ON \
-DLINKSTATIC:BOOL=OFF \
-DOpenGL_GL_PREFERENCE=GLVND \
-DSTOP_ON_WARNING=OFF \
-DUSE_EXTERNAL_PUGIXML:BOOL=ON \
-DUSE_FFMPEG:BOOL=OFF \
-DUSE_OPENCV:BOOL=ON \
-DUSE_OPENSSL:BOOL=ON \
-DUSE_PYTHON:BOOL=OFF  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1725466894
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/oiio
cp %{_builddir}/OpenImageIO-%{version}/LICENSE.md %{buildroot}/usr/share/package-licenses/oiio/7df059597099bb7dcf25d2a9aedfaf4465f72d8d || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
