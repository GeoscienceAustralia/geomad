# Copyright (c) 2018-2025 Geoscience Australia
# SPDX-License-Identifier: Apache-2.0
import numpy.testing as npt
import numpy as np
import geomad
import joblib
import pytest


class TestPixelCompositeMosaic:

    data = joblib.load('data/landchar-small.pkl')

    def test_data(self):
        assert self.data.shape == (200, 200, 8, 18)
        assert self.data.dtype == np.float32

    def test_nangeomedian(self):
        gm = geomad.nangeomedian_pcm(self.data)
        assert gm.shape == (200, 200, 8)

    def test_nangeomedian_fixed(self):
        fixeddata = (self.data * 10000).astype(np.int16)
#        fixeddata[1,1,0,:] = -999
        fgm = geomad.nangeomedian_pcm(fixeddata)
        gm = geomad.nangeomedian_pcm(self.data) * 10000
        npt.assert_approx_equal(np.nanmean(fgm), np.nanmean(gm),
                                significant=4)

    def test_nangeomedian_ro(self):
        data = self.data.copy()
        data.setflags(write=False)
        gm = geomad.nangeomedian_pcm(data)
        assert gm.shape == (200, 200, 8)

    def test_nangeomedian_baddata(self):
        baddata = self.data[:3,:3,:,:].copy()
        baddata[1,1,0,:] = np.nan
        gm = geomad.nangeomedian_pcm(baddata)
        assert np.isnan(gm[1,1,0])

class TestMedianAbsoluteDeviation:

    data = joblib.load('data/landchar-small.pkl')
    gm = geomad.nangeomedian_pcm(data)

    def test_emad(self):
        emad = geomad.emad_pcm(self.data, self.gm)
        assert emad.shape == (200, 200)

    def test_emad_uint16(self):
        stat = geomad.emad_pcm(self.data, self.gm)
        intdata = (self.data * 10000).astype(np.uint16)
        intdata[1,1,0,:] = 0
        intstat = geomad.emad_pcm(intdata, self.gm, nodata=0)
        npt.assert_approx_equal(np.nanmean(stat),
                                np.nanmean(intstat),
                                significant=4)

    def test_emad_baddata(self):
        baddata = self.data[:3,:3,:,:].copy()
        baddata[1,1,0,:] = np.nan
        emad = geomad.emad_pcm(baddata, self.gm)
        print(emad.shape)
        assert np.isnan(emad[1,1])

    def test_smad(self):
        smad = geomad.smad_pcm(self.data, self.gm)
        assert smad.shape == (200, 200)

    def test_smad_uint16(self):
        stat = geomad.smad_pcm(self.data, self.gm)
        intdata = (self.data * 10000).astype(np.uint16)
        intdata[1,1,0,:] = 0
        intstat = geomad.smad_pcm(intdata, self.gm, nodata=0)
        npt.assert_approx_equal(np.nanmean(stat),
                                np.nanmean(intstat),
                                significant=4)

    def test_smad_baddata(self):
        baddata = self.data[:3,:3,:,:].copy()
        baddata[1,1,0,:] = np.nan
        smad = geomad.smad_pcm(baddata, self.gm)
        assert np.isnan(smad[1,1])

    def test_bcmad(self):
        bcmad = geomad.smad_pcm(self.data, self.gm)
        assert bcmad.shape == (200, 200)

    def test_bcmad_uint16(self):
        stat = geomad.bcmad_pcm(self.data, self.gm)
        intdata = (self.data * 10000).astype(np.uint16)
        intdata[1,1,0,:] = 0
        intstat = geomad.bcmad_pcm(intdata, self.gm, nodata=0)
        npt.assert_approx_equal(np.nanmean(stat),
                                np.nanmean(intstat),
                                significant=4)

    def test_bcmad_baddata(self):
        baddata = self.data[:3,:3,:,:].copy()
        baddata[1,1,0,:] = np.nan
        bcmad = geomad.smad_pcm(baddata, self.gm)
        assert np.isnan(bcmad[1,1])
