// Code generated by MockGen. DO NOT EDIT.
// Source: github.com/scionproto/scion/go/hidden_path_srv/internal/hpsegreq (interfaces: Fetcher)

// Package mock_hpsegreq is a generated GoMock package.
package mock_hpsegreq

import (
	context "context"
	gomock "github.com/golang/mock/gomock"
	path_mgmt "github.com/scionproto/scion/go/lib/ctrl/path_mgmt"
	snet "github.com/scionproto/scion/go/lib/snet"
	reflect "reflect"
)

// MockFetcher is a mock of Fetcher interface
type MockFetcher struct {
	ctrl     *gomock.Controller
	recorder *MockFetcherMockRecorder
}

// MockFetcherMockRecorder is the mock recorder for MockFetcher
type MockFetcherMockRecorder struct {
	mock *MockFetcher
}

// NewMockFetcher creates a new mock instance
func NewMockFetcher(ctrl *gomock.Controller) *MockFetcher {
	mock := &MockFetcher{ctrl: ctrl}
	mock.recorder = &MockFetcherMockRecorder{mock}
	return mock
}

// EXPECT returns an object that allows the caller to indicate expected use
func (m *MockFetcher) EXPECT() *MockFetcherMockRecorder {
	return m.recorder
}

// Fetch mocks base method
func (m *MockFetcher) Fetch(arg0 context.Context, arg1 *path_mgmt.HPSegReq, arg2 *snet.UDPAddr) ([]*path_mgmt.HPSegRecs, error) {
	m.ctrl.T.Helper()
	ret := m.ctrl.Call(m, "Fetch", arg0, arg1, arg2)
	ret0, _ := ret[0].([]*path_mgmt.HPSegRecs)
	ret1, _ := ret[1].(error)
	return ret0, ret1
}

// Fetch indicates an expected call of Fetch
func (mr *MockFetcherMockRecorder) Fetch(arg0, arg1, arg2 interface{}) *gomock.Call {
	mr.mock.ctrl.T.Helper()
	return mr.mock.ctrl.RecordCallWithMethodType(mr.mock, "Fetch", reflect.TypeOf((*MockFetcher)(nil).Fetch), arg0, arg1, arg2)
}
